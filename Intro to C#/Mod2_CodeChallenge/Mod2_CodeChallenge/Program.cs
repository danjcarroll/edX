using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod2_CodeChallenge
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int i = 1; i <= 8; i++)
            {
                string square1 = "X";
                string square2 = "O";

                if (i % 2 == 0)
                {
                    square1 = "O";
                    square2 = "X";
                }

                for (int j = 1; j <=4; j++)
                {
                    Console.Write(square1 + square2);
                }
                Console.WriteLine();
            }
        }
    }
}
