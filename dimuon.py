import ROOT as R

f = R.TFile("test_data/events.root")
t = f.Get("events")
n = t.GetEntries()
print "Number of events =", str(n)
