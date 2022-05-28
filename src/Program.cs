using System;
using System.Collections.Generic;

namespace PokemonGame
{
    class Program
    {
        public static void Main(string[] args)
        {
          Initalise.InitalisePokeballs();
                Display.MainMenu();
                while (true)
                {
                    Console.Write("Please only enter [1,2,3,4,5,6,7] or Q to quit: ");
                    switch (Console.ReadLine()!.Trim().ToLower())
                    {

                        case "1":
                            Options.AddingPokemon();
                            break;
                        case "2":
                            Options.DisplayPokemon();
                            break;
                        case "3":
                            Options.CanBeEvolved();
                            break;
                        case "4":
                            Options.EvolvePokemon();
                            break;
                        case "5":
                            Options.PokemonBattle();
                            break;
                        case "6":
                            Options.Gacha();
                            break;
                        case "7":
                            Options.GetPokeballs();
                            break;
                        case "q":
                            Environment.Exit(0);
                            break;

                        default:
                            Console.WriteLine("No proper query");
                            break;

                    }
                }

            
        }
    }
}
