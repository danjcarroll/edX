using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_Mod1_Lab1
{
    class Program
    {
    
        static void Main(string[] args)
        {
            var Car1 = new Car();

            Car1.Color = "Quicksand";
            Car1.Year = 2017;
            Car1.Mileage = 16023;

            // Output to the console window
            Console.WriteLine($"This car is painted {Car1.Color}, was built in {Car1.Year}, and " +
                $"has {Car1.Mileage} miles on it.");
            
        }
    }


    // Declaring the Car() Class
    // This class has 3 properties
    public class Car
    {
        //Defining properties
        public string Color { get; set; }
        public int Year { get; set; }
        public int Mileage { get; set; }
    }
}
