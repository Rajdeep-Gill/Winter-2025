package lab5.b01.RajdeepGill.entity;
import lab5.b01.RajdeepGill.logic.NetworkSimulator;
public class Entity3 extends Entity
{    
    // Perform any necessary initialization in the constructor
    public Entity3()
    {
        // Fill in distances with 999, then update local map
        for (int i = 0; i < distanceTable.length; i++) {
            for (int j = 0; j < distanceTable[i].length; j++) {
                distanceTable[i][j] = 999;
            }
        }

        distanceTable[0][0] = 7; // from 3 to 0 via 0
        distanceTable[2][2] = 2; // from 3 to 2 via 2

        minCosts[0] = 7;
        minCosts[1] = 999;
        minCosts[2] = 2;
        minCosts[3] = 0;
        
        Packet to_p0 = new Packet(3, 0, minCosts);
        Packet to_p2 = new Packet(3, 2, minCosts);

        NetworkSimulator.toLayer2(to_p0);
        NetworkSimulator.toLayer2(to_p2);
        printDT();
    }
    
    // Handle updates when a packet is received.  Students will need to call
    // NetworkSimulator.toLayer2() with new packets based upon what they
    // send to update.  Be careful to construct the source and destination of
    // the packet correctly.  Read the warning in NetworkSimulator.java for more
    // details.
    public void update(Packet p)
    {        
        int source = p.getSource();

        boolean isChanged = false;

        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            int new_cost = p.getMincost(i) + distanceTable[source][source]; // Get to the source of the distance vector from entity 0 via i
            int curr_cost = distanceTable[i][source]; // Get the current cost to entity i from entity 0
            if (new_cost < curr_cost) {
                distanceTable[i][source] = new_cost;
                minCosts[i] = new_cost;
                isChanged = true;
            }
        }

        if (isChanged) {
            Packet to_p0 = new Packet(3, 0, minCosts);
            Packet to_p2 = new Packet(3, 2, minCosts);

            NetworkSimulator.toLayer2(to_p0);
            NetworkSimulator.toLayer2(to_p2);
        }

        printDT();

    }
    
    public void linkCostChangeHandler(int whichLink, int newCost)
    {
    }
    
    public void printDT()
    {
        System.out.println("         via");
        System.out.println(" D3 |   0   2");
        System.out.println("----+--------");
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++)
        {
            if (i == 3)
            {
                continue;
            }
            
            System.out.print("   " + i + "|");
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j += 2)
            {
               
                if (distanceTable[i][j] < 10)
                {    
                    System.out.print("   ");
                }
                else if (distanceTable[i][j] < 100)
                {
                    System.out.print("  ");
                }
                else 
                {
                    System.out.print(" ");
                }
                
                System.out.print(distanceTable[i][j]);
            }
            System.out.println();
        }
    }
}
