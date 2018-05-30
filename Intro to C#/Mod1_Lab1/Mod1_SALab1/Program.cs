using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mod1_SALab1
{
    class Program
    {
        static void Main(string[] args)
        {
            // student information
            string studentFirstName;
            string studentLastName;
            DateTime studentBirthDate;
            string studentAddress1;
            string studentAddress2;
            string studentCity;
            string studentState;
            int studentZip; //assumes no +4 digits
            string studentCountry;

            // teacher information
            string teacherFirstName;
            string teacherLastName;
            DateTime teacherBirthDate;
            string teacherAddress1;
            string teacherAddress2;
            string teacherCity;
            string teacherState;
            int teacherZip; //assumes no +4 digits
            string teacherCountry;

            // UProgram Information
            string programName;
            string deptHead;
            string degrees;

            // Degree information
            string degreeName;
            int creditsRequired;

            // Course information
            string courseName;
            int credits;
            int duration;  //weeks
            string teacher;


            studentFirstName = "Jimbo";
            studentLastName = "Lambert";
            studentBirthDate = new DateTime(2001, 03, 20);
            studentAddress1 = "123 Main Street";
            studentAddress2 = "Suite 1001";
            studentCity = "Smallville";
            studentCountry = "Eurasia";
            studentZip = 889922;

            teacherFirstName = "Roger";
            teacherLastName = "Smithyvelle";
            teacherBirthDate = new DateTime(1971, 06, 06);
            teacherAddress1 = "57463 Guggy Lane";
            teacherAddress2 = "Apt 44";
            teacherCity = "Smallville";
            teacherCountry = "Eurasia";
            teacherZip = 889911;

            programName = "Web Dev";
            deptHead = "Bjorn Lambda";
            degrees = "all";

            degreeName = "Computer Science";
            credits = 3;
            duration = 8;
            teacher = teacherFirstName + " " + teacherLastName;

            Console.WriteLine("{0} {1}", studentFirstName, studentLastName);
            Console.WriteLine($"Born on {studentBirthDate}");
            Console.WriteLine("{0}, {1}", studentAddress1, studentAddress2);
            Console.WriteLine("{0} {1}, {2}", studentCity, studentZip, studentCountry);

            Console.WriteLine("{0} {1}", teacherFirstName, teacherLastName);
            Console.WriteLine($"Born on {teacherBirthDate}");
            Console.WriteLine("{0}, {1}", teacherAddress1, teacherAddress2);
            Console.WriteLine("{0} {1}, {2}", teacherCity, teacherZip, teacherCountry);

            Console.WriteLine("The " + programName + "Program is led by " + deptHead + " and is good for " + degrees + "degrees");

            Console.WriteLine("You will receive {0} credits for the {1} week course", credits, duration);
            Console.WriteLine("This will satisfy a requirement for the {0} degree", degreeName);
            Console.WriteLine($"The course is taught by {teacher}");

        }
    }
}
