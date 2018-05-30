using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod2_Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            //Request user input with ReadLine()
            Console.WriteLine("Please enter an integer value and press Enter. ");

            //Assign the enterd value to the variable input
            //convert input to integer before using
            int input = Int32.Parse(Console.ReadLine());

            //Check to see if the nuber is even
            if(input % 2 == 0)
            {
                Console.WriteLine("The entered number was an even number.");
            }
            else
            {
                Console.WriteLine("The entered number was an odd number.");
            }
        }
    }
}
