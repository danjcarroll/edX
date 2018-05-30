using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod3_Demo1
{
    class Program
    {
        static void Main(string[] args)
        {
            #region Methods

            PrintSomething();

            int first = 25;
            int second = 2;
            string sValue;

            //This method returns a single value
            int result = Sum(first, second);
            Console.WriteLine("The sum of {0} and {1} is: {2}", first, second, result);

            //This method returns multiple values
            //This method uses 'out' keyword

            ReturnMultiOut(out first, out sValue);
            Console.WriteLine("{0}, {1}", first.ToString(), sValue);

            //This method returns multiple values
            //This method uses 'ref' keyword
            sValue = ""; //need to initialize value with a value
            ReturnMultiRef(ref first, ref sValue);
            Console.WriteLine("{0}, {1}", first.ToString(), sValue);


            // Using named parameters
            // This example mixes the order
            Area(length: 30, width: 50);
            // Without named parameters, it needs to be in correct order
            Area(50, 30);

            // Using optional parameters
            OptionalParams(10, 20);

            OptionalParams(3, 4, "woohoo");


            #endregion

        }

        #region Called Methods

        static void PrintSomething()
        {
            Console.WriteLine("PrintSomething() method was called");
        }

        static int Sum(int value1, int value2)
        {
            return value1 + value2;
        }

        static void ReturnMultiOut(out int i, out string s)
        {
            i = 33;
            s = "using out";
        }

        static void ReturnMultiRef(ref int i, ref string s)
        {
            i = 16;
            s = "using ref";
        }

        static void Area(int width, int length)
        {
            Console.WriteLine("The area is {0}", length * width);
        }

        static void OptionalParams(int one, int two, string s = "default text")
        {
            Console.WriteLine("{0}, {1}, {2}", one, two, s);
        }

        #endregion
    }
}
