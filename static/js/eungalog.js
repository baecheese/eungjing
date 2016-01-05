        window.addEventListener("load", function () {
            setDeleteLogEvent();
        }, false);

        function setDeleteLogEvent () {
            var buttons = document.body.querySelectorAll('.deleteButton');
            [].forEach.call(buttons, function(button) {
                button.addEventListener("click", function(e) {
                    e.preventDefault();
                    deleteLog(e);
                }, false);
            });
        }

        function deleteLog (event) {
            var logId = event.target.parentElement.querySelector('.hiddenId').value;
            event.target.parentElement.style.backgroundColor = "yellow";
            alert('선택하신 역사를 삭제합니다.');
            fetch("/eungalog/"+logId, { method: "DELETE" })
                    .then(function(res) {
                        if (res.ok) {
                            alert('하나의 역사가 사라졌습니다.');
                            location.href='/';
                        } else {
                            alert("역사를 지우는데 실패했습니다.");
                            console.log('failed log delete')
                        }
                    }
            );
        };