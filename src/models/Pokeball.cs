namespace PokemonGame
{
    public class Pokeball
    {
        public Pokeball()
        {

        }

        public Pokeball(int count)
        {
            Chance = 0.95;
            Name = "Pokeball";
            Counter = count;

        }

        public int Id {get;set;}
        public double  Chance {get;set;}
        public string? Name {get;set;}
        public int Counter {get;set;}
    }
}