using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace PokemonGame
{

    
    public class PokemonContext : DbContext
    {
        public DbSet<Pokemon> Pokemons { get; set; } = null!; //null forgiving operator to remove warning of EFCore
        public DbSet<Pikachu> Pikachus { get; set; } = null!;
        public DbSet<Eevee> Evees { get; set; } = null!;
        public DbSet<Charmander> Charmanders { get; set; } = null!;
        public DbSet<Yuuki>  Yuukis { get; set; } = null!;
        public DbSet<Pokeball> Pokeballs {get;set;} = null!;

        public string DbPath { get; }

    

        public PokemonContext()
        {
            var folder = Environment.SpecialFolder.LocalApplicationData;
            var path = Environment.GetFolderPath(folder);
            DbPath = System.IO.Path.Join(path, "Pokemon.db");
            Database.EnsureCreated();
        

        }

        protected override void OnConfiguring(DbContextOptionsBuilder options) => options.UseSqlite($"Data Source = {DbPath}");

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Pokemon>().Property(self => self.EvolutionLimit).HasDefaultValue(100);
            modelBuilder.Entity<Pokemon>().Property(self => self.HasEvolved).HasDefaultValue(0);
        
            

        }



    }

}