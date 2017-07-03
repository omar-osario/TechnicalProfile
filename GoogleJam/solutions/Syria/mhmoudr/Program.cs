using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace A
{
    class Program
    {
        static string dir = @"C:\Users\Mahmoud\Projects\GoogleJAM\A\";
        static void Main(string[] args)
        {
            var dic = createDictionary();
            Solve(dic);
            Console.ReadKey();
        }
        static void Solve(Dictionary<char, char> dictionary)
        {
            StreamReader ir = File.OpenText(dir + "input.txt");
            StreamWriter or = File.CreateText(dir + "output.txt");
            int count = int.Parse(ir.ReadLine());
            for (int i = 0; i < count; i++)
            {
                var iline = ir.ReadLine();
                var oline = new StringBuilder(iline.Length);
                foreach (var ic in iline)
                {
                    oline.Append(dictionary[ic]);
                }
                or.WriteLine(string.Format("Case #{0}: {1}",i+1,oline.ToString()));
            }
            ir.Close();
            or.Close();
        }
        static Dictionary<char, char> createDictionary()
        {
            System.IO.StreamReader ir = System.IO.File.OpenText(dir + "i.txt");
            System.IO.StreamReader or = System.IO.File.OpenText(dir + "o.txt");
            var dictionary = new Dictionary<char, char>();
            var alpha = " abcdefghijklmnopqrstuvwxyz";
            foreach (var item in alpha)
                dictionary.Add(item, ' ');
            for (int i = 0; i < 3; i++)
            {
                var il = ir.ReadLine();
                var ol = or.ReadLine();
                for (int j = 0; j < il.Length; j++)
                {
                    if (dictionary[il[j]] != ' ' && dictionary[il[j]] != ol[j])
                        throw new Exception("error");
                    dictionary[il[j]] = ol[j];
                }
            }
            ir.Close();
            or.Close();
            // cover the missing chars, in case of failer switch them back 
            dictionary['z'] = 'q'; // as mentioned in the text example 
            dictionary['q'] = 'z';

            foreach (var dic in dictionary)
            {
                Console.WriteLine(dic.Key + ":" + dic.Value);
            }
            return dictionary;
        }
    }
}
