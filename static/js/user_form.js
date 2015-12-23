window.addEventListener("load", function() {
	var submitForm = document.querySelector("form.join-box")
	submitForm.addEventListener("submit", function(e) {
		e.preventDefault()
		var joinForm = document.querySelector(".join-box")
		var user = {
			"name" : joinForm.querySelector("#id").value
			, "password" : joinForm.querySelector("#password").value
			, "hint_Q" : joinForm.querySelector("#hintQ").value
           , "hint_A" : joinForm.querySelector("#hint_A").value
           , "job" : joinForm.querySelector("#job").value
           , "smoking" : (function () {
        	   		var value;
        	   		[].forEach.call(joinForm.querySelectorAll(".radio"), function(el) {
        	   		if (el.checked === true) {
        	   			value = el.value;
                    }
             });
           return value;
           })()
       }

		fetch("/user", {
                method: "POST",
                headers: {
                    'Accept': 'application/json, text/plain, */*'
                    , "Content-Type": "application/json"
                },
                body: JSON.stringify(user)
            }).then(function(res) {
                if (res.ok) {
                    alert("회원가입에 성공했습니다!")
                    location.href='/';
                } else {
                    alert("아이디 중복 등의 이유로 회원가입에 실패했습니다.");
                }
            });
	        })
}, false)