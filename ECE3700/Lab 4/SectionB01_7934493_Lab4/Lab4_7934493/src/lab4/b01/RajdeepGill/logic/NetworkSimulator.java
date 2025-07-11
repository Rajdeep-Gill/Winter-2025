package lab4.b01.RajdeepGill.logic;

import java.util.Vector;

import lab4.b01.RajdeepGill.entity.Event;
import lab4.b01.RajdeepGill.entity.Message;
import lab4.b01.RajdeepGill.entity.Packet;

import java.util.Enumeration;
import java.io.*;

public abstract class NetworkSimulator
{
    // This constant controls the maximum size of the buffer in a Message
    // and in a Packet
    public static final int MAXDATASIZE = 20;
    
    // These constants are possible events
    public static final int TIMERINTERRUPT = 0;
    public static final int FROMLAYER5 = 1;
    public static final int FROMLAYER3 = 2;
    
    // These constants represent our sender and receiver 
    public static final int A = 0;
    public static final int B = 1;

    private int maxMessages;
    private double lossProb;
    private double corruptProb;
    private double avgMessageDelay;
    protected int traceLevel;
    private EventList eventList;
    private FileWriter outFile;

    private OSIRandom rand;

    private int nSim;
    private int nToLayer3;
    private int nLost;
    private int nCorrupt;
    private double time;
    
    
    protected abstract void aOutput(Message message);
    protected abstract void aInput(Packet packet);
    protected abstract void aTimerInterrupt();
    protected abstract void aInit();

    protected abstract void Simulation_done();

    protected abstract void bInput(Packet packet);
    protected abstract void bInit();
    
    public NetworkSimulator(int numMessages,
                            double loss,
                            double corrupt,
                            double avgDelay,
                            int trace,
                            int seed)
    {
        maxMessages = numMessages;
        lossProb = loss;
        corruptProb = corrupt;
        avgMessageDelay = avgDelay;
        traceLevel = trace;
        eventList = new EventListImpl();
        rand = new OSIRandom(seed);
	try{
	    outFile = new FileWriter("OutputFile");
	}catch (Exception e) {e.printStackTrace();}

        nSim = 0;
        nToLayer3 = 0;
        nLost = 0;
        nCorrupt = 0;
        time = 0;
    }
    
    public void runSimulator()
    {
        Event next;
        
        // Perform any student-required initialization
        aInit();
        bInit();
        
        // Start the whole thing off by scheduling some data arrival
        // from layer 5
        generateNextArrival();
        
        // Begin the main loop
        while (true)
        {
            // Get our next event
            next = eventList.removeNext();
            if (next == null)
            {
                break;
            }
            
            if (traceLevel >= 2)
            {
                System.out.println();
                System.out.print("EVENT time: " + next.getTime());
                System.out.print("  type: " + next.getType());
                System.out.println("  entity: " + next.getEntity());
            }
            
            // Advance the simulator's time
            time = next.getTime();
            
            // Perform the appropriate action based on the event 
            switch (next.getType())
            {
                case TIMERINTERRUPT:
                    if (next.getEntity() == A)
                    {
                        aTimerInterrupt();
                    }
                    else
                    {
                        System.out.println("INTERNAL PANIC: Timeout for " +
                                           "invalid entity");
                    }
                    break;
                    
                case FROMLAYER3:
                    if (next.getEntity() == A)
                    {
                        aInput(next.getPacket());
                    }
                    else if (next.getEntity() == B)
                    {
                        bInput(next.getPacket());
                    }
                    else
                    {
                        System.out.println("INTERNAL PANIC: Packet has " +
                                           "arrived for unknown entity");
                    }
                    
                    break;
                    
                case FROMLAYER5:
                    
                    // If a message has arrived from layer 5, we need to
                    // schedule the arrival of the next message
                    generateNextArrival();
                    
                    char[] nextMessage = new char[MAXDATASIZE];
                    
                    // Now, let's generate the contents of this message
                    char j = (char)((nSim % 26) + 97);
                    for (int i = 0; i < MAXDATASIZE; i++)
                    {
                        nextMessage[i] = j;
                    }
                    
                    // Increment the message counter
                    nSim++;

                    // If we've reached the maximum message count, exit the main loop
		    if (nSim == maxMessages+1)
			break;
                    
                    // Let the student handle the new message
                    aOutput(new Message(new String(nextMessage)));
                    break;
                    
                default:
                    System.out.println("INTERNAL PANIC: Unknown event type");
            }
	    if (nSim == maxMessages+1)
		break;
        }
        System.out.println("Simulator terminated at time "+getTime());
        Simulation_done();
	try{
	    outFile.flush();
	    outFile.close();
	}catch (Exception e) {e.printStackTrace();}
    }
    
    /* Generate the next arrival and add it to the event list */
    private void generateNextArrival()
    {
        if (traceLevel > 2)
        {
            System.out.println("generateNextArrival(): called");
        }
        
        // arrival time 'x' is uniform on [0, 2*avgMessageDelay]
        // having mean of avgMessageDelay.  Should this be made
        // into a Gaussian distribution? 
        double x = 2 * avgMessageDelay * rand.nextDouble(0);
        Event next = new Event(time + x, FROMLAYER5, A);
                
        eventList.add(next);
        if (traceLevel > 2)
        {
            System.out.println("generateNextArrival(): time is " + time);
            System.out.println("generateNextArrival(): future time for " +
                               "event " + next.getType() + " at entity " +
                               next.getEntity() + " will be " +
                               next.getTime());
        }
        
    }
    
    protected void stopTimer(int entity)
    {
        if (traceLevel > 2)
        {
            System.out.println("stopTimer: stopping timer at " + time);
        }

        Event timer = eventList.removeTimer(entity);

        // Let the student know they are attempting to cancel a non-existant 
        // timer
        if (timer == null)
        {
            System.out.println("stopTimer: Warning: Unable to cancel your " +
                               "timer");
        }        
    }
    
    protected void startTimer(int entity, double increment)
    {
        if (traceLevel > 2)
        {
            System.out.println("startTimer: starting timer at " + time);
        }

        Event t = eventList.removeTimer(entity);        

        if (t != null)
        {
            System.out.println("startTimer: Warning: Attempting to start a " +
                               "timer that is already running");
            eventList.add(t);
            return;
        }
        else
        {
            Event timer = new Event(time + increment, TIMERINTERRUPT, entity);
            eventList.add(timer);
        }
    }    
    
    protected void toLayer3(int callingEntity, Packet p)
    {
        nToLayer3++;
        
        int destination;
        double arrivalTime;
        Packet packet = new Packet(p);
    
        if (traceLevel > 2)
        {
            System.out.println("toLayer3: " + packet);
        }

        // Set our destination
        if (callingEntity == A)
        {
            destination = B;
        }
        else if (callingEntity == B)
        {
            destination = A;
        }
        else
        {
            System.out.println("toLayer3: Warning: invalid packet sender");
            return;
        }

        // Simulate losses
        if (rand.nextDouble(1) < lossProb)
        {
            nLost++;
            
            if (traceLevel > 0)
            {
                System.out.println("toLayer3: packet being lost");
            }
            
            return;
        }
        
        // Decide when the packet will arrive.  Since the medium cannot
        // reorder, the packet will arrive 1 to 10 time units after the
        // last packet sent by this sender
        arrivalTime = eventList.getLastPacketTime(destination);
        
        if (arrivalTime <= 0.0)
        {
            arrivalTime = time;
        }
        
        arrivalTime = arrivalTime + 1 + (rand.nextDouble(2) * 9);

        // Simulate corruption
        if (rand.nextDouble(3) < corruptProb)
        {
            nCorrupt++;
            
            if (traceLevel > 0)
            {
                System.out.println("toLayer3: packet being corrupted");
            }
            
            double x = rand.nextDouble(4);
            if (x < 0.75)
            {
                String payload = packet.getPayload();
                
		if (payload.length()>0)
                
		    payload = "?" + payload.substring(payload.length() - 1);
		
		else payload = "?";
                
                packet.setPayload(payload);
            }
            else if (x < 0.875)
            {
                packet.setSeqnum(999999);
            }
            else
            {
                packet.setAcknum(999999);
            }
        }
        

        // Finally, create and schedule this event
        if (traceLevel > 2)
        {
            System.out.println("toLayer3: scheduling arrival on other side");
        }
        Event arrival = new Event(arrivalTime, FROMLAYER3, destination, packet);
        eventList.add(arrival);
    }
    
    protected void toLayer5(String dataSent)
    {
	try{
	    outFile.write(dataSent,0,MAXDATASIZE);
	    outFile.write('\n');
	}catch (Exception e) {e.printStackTrace();}
    }
    
    protected double getTime()
    {
        return time;
    }
    
    protected void printEventList()
    {
        System.out.println(eventList.toString());
    }

    
}
