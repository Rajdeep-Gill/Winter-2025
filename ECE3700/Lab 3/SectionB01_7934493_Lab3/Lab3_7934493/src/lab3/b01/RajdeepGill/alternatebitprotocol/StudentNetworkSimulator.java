package lab3.b01.RajdeepGill.alternatebitprotocol;

import lab3.b01.RajdeepGill.entity.Message;
import lab3.b01.RajdeepGill.entity.Packet;
import lab3.b01.RajdeepGill.logic.NetworkSimulator;

public class StudentNetworkSimulator extends NetworkSimulator {

    /*
     * Predefined Constants (static member variables):
     *
     * int MAXDATASIZE : the maximum size of the Message data and
     * Packet payload
     *
     * int A : a predefined integer that represents entity A
     * int B : a predefined integer that represents entity B
     *
     * Predefined Member Methods:
     *
     * void stopTimer(int entity):
     * Stops the timer running at "entity" [A or B]
     * void startTimer(int entity, double increment):
     * Starts a timer running at "entity" [A or B], which will expire in
     * "increment" time units, causing the interrupt handler to be
     * called. You should only call this with A.
     * void toLayer3(int callingEntity, Packet p)
     * Puts the packet "p" into the network from "callingEntity" [A or B]
     * void toLayer5(String dataSent)
     * Passes "dataSent" up to layer 5
     * double getTime()
     * Returns the current time in the simulator. Might be useful for
     * debugging.
     * int getTraceLevel()
     * Returns TraceLevel
     * void printEventList()
     * Prints the current event list to stdout. Might be useful for
     * debugging, but probably not.
     *
     *
     * Predefined Classes:
     *
     * Message: Used to encapsulate a message coming from layer 5
     * Constructor:
     * Message(String inputData):
     * creates a new Message containing "inputData"
     * Methods:
     * boolean setData(String inputData):
     * sets an existing Message's data to "inputData"
     * returns true on success, false otherwise
     * String getData():
     * returns the data contained in the message
     * Packet: Used to encapsulate a packet
     * Constructors:
     * Packet (Packet p):
     * creates a new Packet that is a copy of "p"
     * Packet (int seq, int ack, int check, String newPayload)
     * creates a new Packet with a sequence field of "seq", an
     * ack field of "ack", a checksum field of "check", and a
     * payload of "newPayload"
     * Packet (int seq, int ack, int check)
     * chreate a new Packet with a sequence field of "seq", an
     * ack field of "ack", a checksum field of "check", and
     * an empty payload
     * Methods:
     * boolean setSeqnum(int n)
     * sets the Packet's sequence field to "n"
     * returns true on success, false otherwise
     * boolean setAcknum(int n)
     * sets the Packet's ack field to "n"
     * returns true on success, false otherwise
     * boolean setChecksum(int n)
     * sets the Packet's checksum to "n"
     * returns true on success, false otherwise
     * boolean setPayload(String newPayload)
     * sets the Packet's payload to "newPayload"
     * returns true on success, false otherwise
     * int getSeqnum()
     * returns the contents of the Packet's sequence field
     * int getAcknum()
     * returns the contents of the Packet's ack field
     * int getChecksum()
     * returns the checksum of the Packet
     * int getPayload()
     * returns the Packet's payload
     *
     */

    /*
     * Please use the following variables in your routines.
     * int WindowSize : the window size
     * double RxmtInterval : the retransmission timeout
     * int LimitSeqNo : when sequence number reaches this value, it wraps around
     */
    public static final int firstSeqNo = 0;
    public static int seqNo = firstSeqNo;
    private int WindowSize; // Not needed
    private double RxmtInterval;
    private int LimitSeqNo;

    // Add any necessary class variables here. Remember, you cannot use
    // these variables to send messages error free! They can only hold
    // state information for A or B.

    // Static variables for ABP
    private static int sequenceNumberA = firstSeqNo;
    private static int sequenceNumberB = firstSeqNo;
    private static int ackNumberA = firstSeqNo; // Flip between 0 and 1
    private static int ackNumberB = firstSeqNo; // Flip between 0 and 1
    private static Packet currentPacket; // For retransmission
    private boolean messageInTransit = false;

    // for throughput calculation
    static int acked_msgs = 0;

    static double start_time = 0;
    static double end_time = 0;

    // Statistics variables
    private int numMessagesDelivered = 0; // Messages successfully delivered
    private double totalTime; // Total simulation time

    // Also add any necessary methods (e.g. checksum of a String)
    // This is the constructor. Don't touch!
    public StudentNetworkSimulator(int numMessages,
            double loss,
            double corrupt,
            double avgDelay,
            int trace,
            int seed,
            int winsize,
            double delay) {
        super(numMessages, loss, corrupt, avgDelay, trace, seed);
        WindowSize = winsize;
        LimitSeqNo = winsize + 1;
        RxmtInterval = delay;
    }

    // Check sum function
    private int checkSum(Packet packet) {
        int sum = 0;
        sum += packet.getSeqnum();
        sum += packet.getAcknum();
        String data = packet.getPayload();

        for (int i = 0; i < data.length(); i++) {
            sum += data.charAt(i);
        }

        return sum;
    }

    // This routine will be called whenever the upper layer at the sender [A]
    // has a message to send. It is the job of your protocol to insure that
    // the data in such a message is delivered in-order, and correctly, to
    // the receiving upper layer.
    protected void aOutput(Message message) {
        // Drop message if another one is in transit
        if (messageInTransit) {
            return;
        }

        // Create packet
        Packet packet = new Packet(sequenceNumberA, 0, 0, message.getData());

        packet.setAcknum(ackNumberA);
        packet.setChecksum(checkSum(packet));

        // Save packet for retransmission
        currentPacket = packet;

        System.out.println("[A] Sending message " + sequenceNumberA);
        messageInTransit = true;
        startTimer(A, RxmtInterval);
        toLayer3(A, packet);
    }

    // This routine will be called whenever a packet sent from the B-side
    // (i.e. as a result of a toLayer3() being done by a B-side procedure)
    // arrives at the A-side. "packet" is the (possibly corrupted) packet
    // sent from the B-side.
    protected void aInput(Packet packet) {
        // Verify checksum
        if (checkSum(packet) != packet.getChecksum()) {
            System.out.println("[A] Corrupted packet, waiting for timeout");
            return; // Corrupted packet, wait for timeout
        }

        // Check ACK number
        System.out.println("[A] Received ACK " + packet.getAcknum());
        acked_msgs++;
        if (packet.getAcknum() == ackNumberA) {
            stopTimer(A);
            messageInTransit = false; // No message in transit
            sequenceNumberA = (sequenceNumberA + 1) % LimitSeqNo; // Update sequence number
            ackNumberA = (ackNumberA + 1) % 2; // Flip ACK number
        }
    }

    // This routine will be called when A's timer expires (thus generating a
    // timer interrupt). You'll probably want to use this routine to control
    // the retransmission of packets. See startTimer() and stopTimer(), above,
    // for how the timer is started and stopped.
    protected void aTimerInterrupt() {
        // Retransmit last packet
        if (messageInTransit) {
            System.out.println("[A] Timeout, resending message " + sequenceNumberA);
            startTimer(A, RxmtInterval);
            toLayer3(A, currentPacket);
        }
    }

    // This routine will be called once, before any of your other A-side
    // routines are called. It can be used to do any required
    // initialization (e.g. of member variables you add to control the state
    // of entity A).
    protected void aInit() {
        System.out.println("[A] Initializing");
        sequenceNumberA = firstSeqNo;
        ackNumberA = firstSeqNo;
        messageInTransit = false;
        start_time = getTime();
    }

    // This routine will be called whenever a packet sent from the B-side
    // (i.e. as a result of a toLayer3() being done by an A-side procedure)
    // arrives at the B-side. "packet" is the (possibly corrupted) packet
    // sent from the A-side.
    protected void bInput(Packet packet) {
        // Verify checksum
        if (checkSum(packet) != packet.getChecksum()) {
            System.out.println("[B] Corrupted packet, ignoring");
            return; // Corrupted packet, ignore it
        }

        // Check ack number
        if (packet.getAcknum() == ackNumberB) {
            numMessagesDelivered++; // Successfully delivered message
            // Deliver to layer 5
            System.out.println("[B] Received message " + sequenceNumberB);
            toLayer5(packet.getPayload());

            // Send ACK
            System.out.println("[B] Sending ACK " + ackNumberB);
            Packet ack = new Packet(0, ackNumberB, 0, "");
            ack.setChecksum(checkSum(ack));
            toLayer3(B, ack);

            // Update expected sequence number and ACK number
            sequenceNumberB = (sequenceNumberB + 1) % LimitSeqNo;
            ackNumberB = (ackNumberB + 1) % 2;
        } else { // Packet was resent by A, so resend previous ack
            int prevAck = (ackNumberB + 1) % 2;
            System.out.println("[B] Resending ACK " + prevAck);
            Packet ack = new Packet(0, prevAck, 0, "");
            ack.setChecksum(checkSum(ack));
            toLayer3(B, ack);
        }
    }

    // This routine will be called once, before any of your other B-side
    // routines are called. It can be used to do any required
    // initialization (e.g. of member variables you add to control the state
    // of entity B).
    protected void bInit() {
        System.out.println("[B] Initializing");
        sequenceNumberB = firstSeqNo;
        ackNumberB = firstSeqNo;
    }

    // Use to print final statistics
    protected void Simulation_done() {
        totalTime = getTime() - start_time;
        double throughput = (double) numMessagesDelivered / totalTime;

        System.out.println("\n=== Simulation Statistics ===");
        System.out.println("Simulation time: " + String.format("%.2f", totalTime));
        System.out.println("Messages Delivered: " + numMessagesDelivered);
        System.out.println("Throughput: " + String.format("%.9f", throughput) + " messages/time unit");
        System.out.println("==========================\n");
    }

}
