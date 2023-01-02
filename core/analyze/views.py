from django.shortcuts import render, redirect

from analyze.analyze import analyze_diabetes
from analyze.forms import DiabetesForm


def test(request):
    if request.method == "POST":
        form = DiabetesForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save_model(int(form.cleaned_data.get('Age')), request.user)
            result, positive, negative, Diabetes_Prediction = analyze_diabetes(
                instance.HighBP, instance.HighChol, instance.CholCheck, instance.BMI, instance.Smoker, instance.Stroke,
                instance.HeartDiseaseorAttack, instance.PhysActivity, instance.Fruits, instance.Veggies,
                instance.HvyAlcoholConsump, instance.AnyHealthcare, instance.NoDocbcCost, instance.GenHlth,
                instance.MentHlth, instance.PhysHlth, instance.DiffWalk, instance.Sex, instance.Age, instance.Education
            )
            instance.Diabetes_012 = Diabetes_Prediction
            instance.result = result
            form.save()
            return redirect('test')
        return redirect('test')
    else:
        form = DiabetesForm()
        return render(request, 'dashboard/test.html', {'form': form})

def results(request):
    pass



