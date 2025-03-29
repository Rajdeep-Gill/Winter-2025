package lab5.b01.RajdeepGill.logic;


import lab5.b01.RajdeepGill.entity.Event;

public interface EventList
{
    public boolean add(Event e);
    public Event removeNext();
    public String toString();
    public double getLastPacketTime(int entityFrom, int entityTo);
}
