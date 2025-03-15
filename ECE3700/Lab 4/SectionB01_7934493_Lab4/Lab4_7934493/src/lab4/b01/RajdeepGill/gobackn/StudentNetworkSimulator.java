package lab4.b01.RajdeepGill.gobackn;

import java.util.LinkedList;

import lab4.b01.RajdeepGill.entity.Message;
import lab4.b01.RajdeepGill.entity.Packet;
import lab4.b01.RajdeepGill.logic.NetworkSimulator;

public class StudentNetworkSimulator extends NetworkSimulator {

    /*
     * Please use the following variables in your routines.
     * int WindowSize : the window size
     * double RxmtInterval : the retransmission timeout
     * int LimitSeqNo : when sequence number reaches this value, it wraps around
     */

    public static final int FirstSeqNo = 0;
    private int WindowSize;
    private double RxmtInterval;
    private int LimitSeqNo;

    // Add any necessary class variables here. Remember, you cannot use
    // these variables to send messages error free! They can only hold
    // state information for A or B.
    // Also add any necessary methods (e.g. checksum of a String)

    private int base; // oldest unacked packet
    private int nextSeqNum; // next sequence number to use
    private int expectedSeqNum; // expected sequence number at receiver
    LinkedList<Packet> window = new LinkedList<Packet>();
    LinkedList<Message> buffer = new LinkedList<Message>();

    // For statistics
    int successPackets = 0;

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
        if (nextSeqNum < base + WindowSize) {
            Packet packet = new Packet(nextSeqNum % LimitSeqNo, 0, 0, message.getData());
            packet.setChecksum(checkSum(packet));
            window.addLast(packet);

            System.out.println("[" + getTime() + "]" + "[A] Sending packet " + nextSeqNum + " Base is " + base);
            toLayer3(A, packet);
            
            if (base == nextSeqNum) {
                startTimer(A, RxmtInterval);
            }
            nextSeqNum++;
        } else {
            buffer.addLast(message);
            System.out.println("[" + getTime() + "]" + "[A] Window full, buffering message");
        }
    }

    // This routine will be called whenever a packet sent from the B-side
    // (i.e. as a result of a toLayer3() being done by a B-side procedure)
    // arrives at the A-side. "packet" is the (possibly corrupted) packet
    // sent from the B-side.
    protected void aInput(Packet packet) {
        if (checkSum(packet) != packet.getChecksum()) {
            System.out.println("[" + getTime() + "]" + "[A] Corrupted ACK received");
            return;
        }

        int ackNum = packet.getAcknum();
        if (ackNum >= base) {
            // Calculate how many packets to remove
            int numToRemove = ackNum - base + 1;
            
            // Remove acknowledged packets from window
            for (int i = 0; i < numToRemove && !window.isEmpty(); i++) {
                window.removeFirst();
                successPackets++;
            }
            
            base = ackNum + 1;
            System.out.println("[" + getTime() + "]" + "[A] Received ACK for packet " + ackNum + " Base is now " + base);

            // Send any buffered packets if window has space
            while (!buffer.isEmpty() && nextSeqNum < base + WindowSize) {
                aOutput(buffer.removeFirst());
            }

            if (base == nextSeqNum) {
                stopTimer(A);
            } else {
                stopTimer(A);
                startTimer(A, RxmtInterval);
            }
        }
    }

    // This routine will be called when A's timer expires (thus generating a
    // timer interrupt). You'll probably want to use this routine to control
    // the retransmission of packets. See startTimer() and stopTimer(), above,
    // for how the timer is started and stopped.
    protected void aTimerInterrupt() {
        if (!window.isEmpty()) {
            startTimer(A, RxmtInterval);
            System.out.println("[" + getTime() + "]" + "[A] Timer interrupt, resending " + window.size() + " packets");
            
            for (Packet packet : window) {
                System.out.println("[" + getTime() + "]" + "[A] Resending packet " + packet.getSeqnum());
                toLayer3(A, packet);
            }
        }
    }

    // This routine will be called once, before any of your other A-side
    // routines are called. It can be used to do any required
    // initialization (e.g. of member variables you add to control the state
    // of entity A).
    protected void aInit() {
        base = 0;
        nextSeqNum = 0;
    }

    // This routine will be called whenever a packet sent from the B-side
    // (i.e. as a result of a toLayer3() being done by an A-side procedure)
    // arrives at the B-side. "packet" is the (possibly corrupted) packet
    // sent from the A-side.
    protected void bInput(Packet packet) {
        if (checkSum(packet) != packet.getChecksum()) {
            System.out.println("[" + getTime() + "]"
                    + "[B] Corrupted packet received");
            if (expectedSeqNum > 0) {
                Packet ackPacket = new Packet(0, expectedSeqNum - 1, 0);
                ackPacket.setChecksum(checkSum(ackPacket));
                toLayer3(B, ackPacket);
            }
            return;
        }

        if (packet.getSeqnum() == expectedSeqNum % LimitSeqNo) {
            toLayer5(packet.getPayload());
            Packet ackPacket = new Packet(0, expectedSeqNum, 0);
            ackPacket.setChecksum(checkSum(ackPacket));
            toLayer3(B, ackPacket);
            System.out.println("[" + getTime() + "]" + "[B] Received in-order packet " + expectedSeqNum);
            expectedSeqNum++;
        } else {
            System.out.println("[" + getTime() + "]" + "[B] Out of order packet " + packet.getSeqnum() + ", expected " + expectedSeqNum);
            if (expectedSeqNum > 0) {
                Packet ackPacket = new Packet(0, expectedSeqNum - 1, 0);
                ackPacket.setChecksum(checkSum(ackPacket));
                toLayer3(B, ackPacket);
            }
        }
    }

    // This routine will be called once, before any of your other B-side
    // routines are called. It can be used to do any required
    // initialization (e.g. of member variables you add to control the state
    // of entity B).
    protected void bInit() {
        expectedSeqNum = 0;
    }

    // Use to print final statistics
    protected void Simulation_done() {
        // Calculate and print statistics
        System.out.println("Protocol: Go-Back-N");
        System.out.println("Window Size: " + WindowSize);
        System.out.println("Number of packets received: " + successPackets);
        double time = getTime();
        System.out.println("Throughput: " + (successPackets / time));
    }

}
