package lab5.b01.RajdeepGill.entity;

import lab5.b01.RajdeepGill.logic.NetworkSimulator;

public class Entity2 extends Entity {
    // Perform any necessary initialization in the constructor
    public Entity2() {
        // Fill in distances with 999, then update local map
        for (int i = 0; i < distanceTable.length; i++) {
            for (int j = 0; j < distanceTable[i].length; j++) {
                distanceTable[i][j] = 999;
            }
        }

        distanceTable[0][0] = 3; // from 2 to 0 via 0
        distanceTable[1][1] = 1; // from 2 to 1 via 1
        distanceTable[2][2] = 0; // self
        distanceTable[3][3] = 2; // from 2 to 3 via 3

        minCosts[0] = 3;
        minCosts[1] = 1;
        minCosts[2] = 0;
        minCosts[3] = 2;

        Packet to_p0 = new Packet(2, 0, minCosts);  
        Packet to_p1 = new Packet(2, 1, minCosts);
        Packet to_p3 = new Packet(2, 3, minCosts);
        
        NetworkSimulator.toLayer2(to_p0);
        NetworkSimulator.toLayer2(to_p1);
        NetworkSimulator.toLayer2(to_p3);

        printDT();
    }

    // Handle updates when a packet is received. Students will need to call
    // NetworkSimulator.toLayer2() with new packets based upon what they
    // send to update. Be careful to construct the source and destination of
    // the packet correctly. Read the warning in NetworkSimulator.java for more
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
            Packet to_p0 = new Packet(2, 0, minCosts);
            Packet to_p1 = new Packet(2, 1, minCosts);
            Packet to_p3 = new Packet(2, 3, minCosts);

            NetworkSimulator.toLayer2(to_p0);
            NetworkSimulator.toLayer2(to_p1);
            NetworkSimulator.toLayer2(to_p3);
        }

        printDT();

    }

    public void linkCostChangeHandler(int whichLink, int newCost) {
    }

    public void printDT() {
        System.out.println();
        System.out.println("           via");
        System.out.println(" D2 |   0   1   3");
        System.out.println("----+------------");
        for (int i = 0; i < NetworkSimulator.NUMENTITIES; i++) {
            if (i == 2) {
                continue;
            }

            System.out.print("   " + i + "|");
            for (int j = 0; j < NetworkSimulator.NUMENTITIES; j++) {
                if (j == 2) {
                    continue;
                }

                if (distanceTable[i][j] < 10) {
                    System.out.print("   ");
                } else if (distanceTable[i][j] < 100) {
                    System.out.print("  ");
                } else {
                    System.out.print(" ");
                }

                System.out.print(distanceTable[i][j]);
            }
            System.out.println();
        }
    }
}
