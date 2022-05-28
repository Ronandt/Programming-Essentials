using System.Collections.Generic;

namespace PokemonGame {
    public abstract class Pokemon
    {
        public int PokemonId { get; set; }
        public string? Name { get; set; }
        public abstract string? Skill {get;set;}
        public int HP {get;set;}
        public int Exp {get;set;}
        public int Atk {get;set;}
        public int HasEvolved {get;set;}
        public int EvolutionLimit {get;set;}

        /*public string? EvolveTo {get;set;}*/
    }

    
}