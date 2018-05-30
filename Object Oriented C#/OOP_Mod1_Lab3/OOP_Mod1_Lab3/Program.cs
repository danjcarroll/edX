using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_Mod1_Lab3
{
    class Program
    {
        static void Main(string[] args)
        {
            var Car1 = new Car();
            Car1.Color = "Quicksand";
            Car1.Year = 2017;
            Car1.Mileage = 14869;

            var Car2 = new Car("Red", 2008);

            // Access static members
            int carCount = Car.CountCars();

            //Output to the console window
            Console.WriteLine($"There are {carCount} cars on inventory right now.");


        }
    }

}
