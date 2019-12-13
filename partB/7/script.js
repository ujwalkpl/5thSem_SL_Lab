function calc() {
var for1 = document.getElementById("form1")
var sum = 0

function grade_cal(num){
    cgpalis = [];
	var grade = ""
	if(num>90){
	grade="Grade S+"
	cgpalis.append(10)
	}
	else if(num>80){
	grade="Grade S"
	cgpalis.append(9)
	}
	else if(num>70){
	grade = "Grade A"
	cgpalis.append(8)
	}
	else if(num>60){
	grade = "Grade B"
	cgpalis.append(7)
	}
	else if(num>50){
	grade = "Grade C"
	cgpalis.append(6)
	}
	else if(num>40){
	grade = "Grade D"
	cgpalis.append(5)
	}
	else {
	grade ="Grade F"
	cgpalis.append(0)
	}
	return grade
	}


for(var i = 0 ;i<for1.length;i++){
document.getElementById("grad"+i).innerHTML = grade_cal(for1[i].value)
sum= sum+parseInt(for1[i].value);
}

cgpa1= sum(cgpalis)/length(cgpalis);

document.getElementById("result").innerHTML = sum
document.getElementById("grade").innerHTML = grade_cal(sum)
document.getElementById("cgpa").innerHTML = cgpa1


}
