using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OOP_Mod1_Lab3
{
    class Car
    {
        public string Color { get; set; }
        public int Year { get; set; }
        public int Mileage { get; set; }

        // Adding a Constructor
        // This constructor instantiates a Car() object while only having the car's color and year
        // information available
        public Car(string color, int year)
        {
            this.Color = color;
            this.Year = year;
            instances++;
        }

        // Adding another Constructor
        // This constructor instantiates a Car() object while only having the car's year and mileage
        // information available
        public Car(int year, int mileage)
        {
            this.Year = year;
            this.Mileage = mileage;
            instances++;
        }

        //Creates integer variable called "instances" and assigns value to 0
        private static int instances = 0;

        public Car()
        {
            //Every time the constructor runs, increment "instances"
            instances++;
        }

        //Declare static member
        public static int CountCars()
        {
            return instances;
        }

    }
}
