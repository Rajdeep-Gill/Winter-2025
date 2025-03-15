package lab4.b01.RajdeepGill.logic;

import lab4.b01.RajdeepGill.entity.Event;

public interface EventList
{
    public boolean add(Event e);
    public Event removeNext();
    public String toString();
    public Event removeTimer(int entity);
    public double getLastPacketTime(int entityTo);
}
