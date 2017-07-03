using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace C
{
    class Program
    {
        static void Main(string[] args)
        {
            var dir = @"C:\Users\Mahmoud\Projects\GoogleJAM\C\";
            StreamReader ir = File.OpenText(dir + "i.txt");
            StreamWriter or = File.CreateText(dir + "o.txt");
            int count = int.Parse(ir.ReadLine());
            for (int i = 0; i < count; i++)
            {
                var line = ir.ReadLine().Split(new[]{' '});
                or.WriteLine(string.Format("Case #{0}: {1}", i + 1, CountRecycled(int.Parse(line[0]), int.Parse(line[1]))));
                or.Flush();
            }
            ir.Close();
            or.Close();
        }
        static int CountRecycled(int A, int B)
        {
            int res = 0;
            for (int i = A; i <= B; i++)
                res += checkAllRecycled(i, B);
            return res;
        }
        static int checkAllRecycled(int m, int n)
        {
            int res = 0;
            List<int> oldRes = new List<int>();
            string A = rountNumber(m.ToString());
            int An = int.Parse(A);
            while (A != m.ToString())
            {
                if (An > m && An <= n)
                    res++;
                A = rountNumber(A);
                An = int.Parse(A);
            }
            return res;
        }
        static string rountNumber(string num)
        {
            if(num.Length<2) 
                return num.ToString();
            var A = num.ToString();
            return A.Substring(1) + A[0];
        }
    }
}
