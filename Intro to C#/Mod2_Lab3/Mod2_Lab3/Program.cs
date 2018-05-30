using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod2_Lab3
{
    class Program
    {
        static void Main(string[] args)
        {
            //Create a simple loop that displays the values of the counter

            for (int counter = 0; counter < 10; counter++)
            {
                Console.WriteLine($"Counter is at: {counter}");
            }

            //Create a nested loop to find prime numbers

            int outer;
            int inner;

            for(outer = 2; outer < 100; outer++)
            {
                for (inner = 2; inner <= (outer / inner); inner++)
                    if ((outer % inner) == 0) break;
                if (inner > (outer / inner))
                    Console.WriteLine("{0} is a prime", outer);
            }
           
        }
    }
}
