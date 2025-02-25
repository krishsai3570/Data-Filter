from django.shortcuts import render

from django.views.generic import TemplateView, View

from myapp.models import Vehicle



class VehicleListView(View):

    def get(self,request,*args,**kwrags):

        qs=Vehicle.objects.all()


        category=request.GET.get("category")

        brand=request.GET.get("brand")

        car_type=request.GET.get("car_type")

        bike_type=request.GET.get("bike_type")

        ownership=request.GET.get("ownership")

        model_min = request.GET.get('year_min')

        model_max = request.GET.get('year_max')

        price_min = request.GET.get('price_min')

        price_max = request.GET.get('price_max')

        km_drive_min = request.GET.get('km_drive_min')

        km_drive_max = request.GET.get('km_drive_max')

        


        if category:
            
            qs=qs.filter(category=category)

        if brand:

            qs=qs.filter(brand=brand)


        if car_type:

            qs=qs.filter(car_type=car_type)

        if bike_type:

            qs=qs.filter(bike_type=bike_type)

        if ownership:

            qs=qs.filter(ownership=ownership)

        if model_min:

            qs = qs.filter(year__gte=model_min)

        if model_max:

            qs = qs.filter(year__lte=model_max)

        if price_min:

            qs = qs.filter(price__gte=price_min)

        if price_max:

            qs = qs.filter(price__lte=price_max)

        if km_drive_min:

            qs = qs.filter(km_drive__gte=km_drive_min)

        if km_drive_max:

            qs = qs.filter(km_drive__lte=km_drive_max)

        if brand:
            qs = qs.filter(brand__icontains=brand)    

        return render(request,"car_list.html",{"data":qs})


class HomeView(TemplateView):
    template_name = "home.html"






