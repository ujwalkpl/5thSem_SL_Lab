function calc() {
var for1 = document.getElementById("form1")
var sum = 0

function grade_cal(num){
	var grade = ""
	if(num>90)
	grade="Grade S+"
	else if(num>80)
	grade="Grade S"
	else if(num>70)
	grade = "Grade A"
	else if(num>60)
	grade = "Grade B"
	else if(num>50)
	grade = "Grade C"
	else if(num>40)
	grade = "Grade D"
	else
	grade ="Grade F"
	return grade
	}


for(var i = 0 ;i<for1.length;i++){
document.getElementById("grad"+i).innerHTML = grade_cal(for1[i].value)
console.log(grade_cal(for1[i].value)) 


sum= sum+parseInt(for1[i].value);
}
document.getElementById("result").innerHTML = sum
document.getElementById("grade").innerHTML = grade_cal(sum)


}
