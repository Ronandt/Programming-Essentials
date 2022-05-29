namespace PokemonGame
{
    public class Initalise
    {
        public static void InitalisePokeballs()
        {
            using (PokemonContext db = new PokemonContext())
            {
                try
                {

                    db.Pokeballs.Where(x => x.Id == 1).First();

                }
                catch (System.InvalidOperationException)
                {
                    db.Pokeballs.Add(new Pokeball(0));
                    db.SaveChanges();
                }
            }
        }
    }
}