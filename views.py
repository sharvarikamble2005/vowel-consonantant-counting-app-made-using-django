from django.shortcuts import render


def home(request):
	if request.method=="POST":
		txt=request.POST.get("txt")

		if len(txt)==0:
			msg="text is empty"
			return render(request,"home.html",{"msg":msg})

		vc=0
		cc=0
		for t in txt:
			if t.isalpha():
				if t in "aeiouAEIOU":
						vc+=1
				else:
						cc+=1
		msg="vc= "+str(vc)+" cc = "+str(cc)
		return render(request,"home.html",{"msg":msg})

	else:
		return render(request,"home.html")