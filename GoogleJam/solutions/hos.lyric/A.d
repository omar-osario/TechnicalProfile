import std.stdio, std.string, std.conv;
import std.algorithm, std.array, std.bigint, std.math, std.range;
import core.thread;

//	Input
string[] tokens;
int tokenId = 0;
string readToken() { for (; tokenId == tokens.length; ) tokens = readln.split, tokenId = 0; return tokens[tokenId++]; }
int readInt() { return to!int(readToken); }
long readLong() { return to!long(readToken); }

//	chmin/chmax
void chmin(T)(ref T t, T f) { if (t > f) t = f; }
void chmax(T)(ref T t, T f) { if (t < f) t = f; }

//	Pair
struct Pair(S, T) {
	S x; T y;
	int opCmp(ref const Pair p) const { return (x < p.x) ? -1 : (x > p.x) ? +1 : (y < p.y) ? -1 : (y > p.y) ? +1 : 0; }
	string toString() const { return "(" ~ to!string(x) ~ ", " ~ to!string(y) ~ ")"; }
}
auto pair(S, T)(S x, T y) { return Pair!(S, T)(x, y); }

//	Array
int binarySearch(T)(T[] as, bool delegate(T) test) {
	int low = -1, upp = as.length; for (; low + 1 < upp; ) { int mid = (low + upp) >> 1; (test(as[mid]) ? low : upp) = mid; } return upp;
}
int lowerBound(T)(T[] as, T val) { return as.binarySearch((T a){ return (a <  val); }); }
int upperBound(T)(T[] as, T val) { return as.binarySearch((T a){ return (a <= val); }); }
T[] unique(T)(T[] as) { T[] bs; foreach (a; as) if (bs == null || bs[$ - 1] != a) bs ~= a; return bs; }

string[] SAMPLE_INPUT = [
	"ejp mysljylc kd kxveddknmc re jsicpdrysi", 
	"rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd", 
	"de kr kd eoya kw aej tysr re ujdr lkgc jv", 
];
string[] SAMPLE_OUTPUT = [
	"our language is impossible to understand", 
	"there are twenty six factorial possibilities", 
	"so it is okay if you want to just give up", 
];
char[char] google, elgoog;

void prepare() {
	foreach (i; 0 .. SAMPLE_INPUT.length) {
		string s = SAMPLE_INPUT[i], t = SAMPLE_OUTPUT[i];
		foreach (j; 0 .. s.length) {
			google[s[j]] = t[j];
			elgoog[t[j]] = s[j];
		}
	}
	for (char c = 'a'; c <= 'z'; ++c) {
		if (c !in google) {
			stderr.writeln("google ", c);
		}
	}
	for (char c = 'a'; c <= 'z'; ++c) {
		if (c !in elgoog) {
			stderr.writeln("elgoog ", c);
		}
	}
	google['q'] = 'z';
	google['z'] = 'q';
}

class Solver : Thread {
	int caseId;
	this(int caseId) {
		this.caseId = caseId;
		super(&main);
	}
	void main() {
		try {
			run;
			stderr.writeln("DONE  Case #", caseId);
		} catch (Throwable e) {
			stderr.writeln("ERROR Case #", caseId, ": ", e.msg);
		} finally {
			stderr.flush;
		}
	}
	
	string S, T;
	
	void run() {
// writeln("S = ",S);
		foreach (c; S) {
			T ~= google[c];
		}
	}
	
	void input() {
		S = readln.chomp;
	}
	
	void output() {
		writeln("Case #", caseId, ": ", T);
		stdout.flush;
	}
}

void main(string[] args) {
	bool parallel = false;
	foreach (arg; args) if (arg == "-p") parallel = true;
	prepare;
	// auto solvers = new Solver[readInt];
	auto solvers = new Solver[to!int(readln.chomp)];
	foreach (caseId, ref solver; solvers) solver = new Solver(caseId + 1);
	if (parallel) {
		foreach (solver; solvers) solver.input, solver.start;
		foreach (solver; solvers) solver.join, solver.output;
	} else {
		foreach (caseId, solver; solvers) {
			solver.input;
			solver.run;
			solver.output;
			stderr.writeln("DONE  Case #", caseId + 1);
			stderr.flush;
		}
	}
}

