window.onload=function(){
    var a=[
    {
        model:"ford",
        name:"Figo",
        year:2015,
        price:750000
    },
    {
        model:"fiat",
        name:"Punto",
        year:2019,
        price:750000
    },
    {
        model:"maruti",
        name:"Swift Dzire",
        year:2017,
        price:550000
    }

    ]

   a.forEach(mouseoverhandler);

   function mouseoverhandler(item,index){
    var b=document.getElementById(item.model)
    b.onmouseover = function(){
         document.getElementById("datatable").removeAttribute('hidden');
        
            document.getElementById("name").innerHTML = item.name;
            document.getElementById("price").innerHTML= item.price;
            document.getElementById("year").innerHTML=item.year;
    }

   }        
};