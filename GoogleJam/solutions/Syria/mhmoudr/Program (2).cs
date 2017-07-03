using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace B
{
    class Program
    {
        class Googler
        {
            public int Score;
            public Triplet Solve(int target, bool IsAllowingSurprising)
            {
                var posibilities = AllTriplets
                    .Where(t => 
                        t.Score == Score 
                        && t.C >= target 
                        && (IsAllowingSurprising || !t.IsSurprising))
                    .OrderBy(t => t.IsSurprising).ToArray();
                foreach (var p in posibilities)
                {
                    if (p.C >= target)
                        return p;
                }
                return null;
            }
        }
        class Triplet
        {
            public int A;
            public int B;
            public int C;
            public int Score;
            public bool IsSurprising;
        }
        static List<Triplet> AllTriplets = new List<Triplet>();
        static void Main(string[] args)
        {
            for (int i = 0; i <= 10; i++)
                for (int j = i; j < i + 3 && j <= 10; j++)
                    for (int k = j; k < i + 3 && k <= 10; k++)
                        AllTriplets.Add(new Triplet() { A = i, B = j, C = k, Score = i + j + k, IsSurprising = (k - i == 2) });
            //foreach (var t in AllTriplets)
            //{
            //    if (t.IsSurprising)
            //        Console.WriteLine(string.Format("{0}:{1},{2},{3}", t.Score, t.A, t.B, t.C));
            //}
            var dir = @"C:\Users\Mahmoud\Projects\GoogleJAM\B\";
            StreamReader ir = File.OpenText(dir + "i.txt");
            StreamWriter or = File.CreateText(dir + "o.txt");
            int count = int.Parse(ir.ReadLine());
            for (int i = 0; i < count; i++)
            {
                var line = ir.ReadLine().Split(new char[] {' '});
                int GooglersNum = int.Parse(line[0]);
                int Surprising = int.Parse(line[1]);
                int TargetScore = int.Parse(line[2]);
                var Googlers = new List<Googler>(GooglersNum);
                int counter = 0;
                for (int j = 0; j < GooglersNum; j++)
                {
                    var g = new Googler() { Score = int.Parse(line[j + 3]) };
                    var t = g.Solve(TargetScore, (Surprising > 0));
                    if (t != null)
                    {
                        if (t.IsSurprising)
                            Surprising--;
                        counter++;
                    }
                }
                or.WriteLine(string.Format("Case #{0}: {1}", i + 1, counter));
            }
            ir.Close();
            or.Close();
        }
    }
}
