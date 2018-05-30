using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod2_Demo
{
    class Program
    {
        static void Main(string[] args)
        {

            #region Decision Statements

            //int condition1;
            //int condition2;
            //int switchCondition;

            //if sample
            //condition1 = 1;
            //if (condition1 == 1)
            //{
            //    Console.WriteLine("Comparison evaluated to true.");
            //}
            //Console.WriteLine("This executes after the if, regardless");

            //if-else sample
            //condition1 = 3;
            //if (condition1 == 1)
            //{
            //    Console.WriteLine("Comparison evaluated to true.");
            //}
            //else
            //{
            //    Console.WriteLine("Comparison evaluated to false.");
            //}

            //if-else if-else example
            //condition1 = 3;
            //condition2 = 2;
            //if (condition1 == 1)
            //{
            //    Console.WriteLine("Conidition 1 is 1");
            //}
            //else if (condition2 == 2)
            //{
            //    Console.WriteLine("Condition 2 is 2.");
            //}
            //else
            //{
            //    Console.WriteLine("Neither triggered.");
            //}

            //switchCondition = 5;
            //switch(switchCondition)
            //    {
            //    case 1:
            //        Console.WriteLine("Value is 1");
            //        break;
            //    case 2:
            //        Console.WriteLine("Value is 2");
            //        break;
            //    case 3:
            //        Console.WriteLine("Value is 3");
            //        break;
            //    default:
            //        Console.WriteLine("Value is " + switchCondition);
            //        break;
            //    }
            #endregion

            #region Repitition Statements

            int whileCounter = 0;
            int doCounter = 5;

            //for loop example

            //Console.WriteLine("for loop");
            //Console.WriteLine();

            //for (int forCounter = 0; forCounter < 10; forCounter++)
            //{
            //    Console.WriteLine("forCounter is at " + forCounter);
            //}

            //Console.WriteLine("while loop");
            //Console.WriteLine();
            //while (whileCounter < 5)
            //{
            //    Console.WriteLine("whileCounter is at " + whileCounter);
            //    whileCounter++;
            //}
        

            Console.WriteLine("do-while loop");
            Console.WriteLine();
            do
            {
                Console.WriteLine("doCounter is at " + doCounter);
                doCounter++;
            } while (doCounter < 5);

            #endregion



        }//main
    }
}
