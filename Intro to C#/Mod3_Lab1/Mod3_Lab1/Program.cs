using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod3_Lab1
{
    class Program
    {
        static void Main(string[] args)
        {
            int result = Sum(20, 40);
            Console.WriteLine($"Calling Sum() with 2 arguments, result is: {result}");

            int result3 = Sum(10, 50, 80);
            Console.WriteLine($"Calling Sum() with 3 arguments, result in: {result3}");

            double dblResult = Sum(20.5, 30.6);
            Console.WriteLine($"Calling Sum() that takes doubles results in: {dblResult}");
        }

        // Sum() method that takes two integer arguments and sums them
        // The method returns no value which is why we use void
        // We also need to use static in the method signature because Main is static
        // and you cannot call a non-static method from a static method
        //static void Sum(int first, int second)
        //{
        //    int sum = first + second;
        //    Console.WriteLine($"The sum of {first} and {second} is: {sum}");
        //}

        static int Sum(int first, int second)
        {
            int sum = first + second;
            return sum;
        }

        static int Sum(int first, int second, int third)
        {
            int sum = first + second + third;
            return sum;
        }

        static double Sum(double first, double second)
        {
            double result = first + second;
            return result;
        }
    }
}
