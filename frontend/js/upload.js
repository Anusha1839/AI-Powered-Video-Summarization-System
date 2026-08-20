console.log("UPLOAD JS LOADED");

var fileInput =
document.getElementById("videoFile");

var fileName =
document.getElementById("fileName");

var summarizeBtn =
document.getElementById("summarizeBtn");

var clearBtn =
document.getElementById("clearBtn");

fileInput.addEventListener(
    "change",
    function () {

        if (fileInput.files.length > 0) {

            fileName.innerText =
            fileInput.files[0].name;

        }

    }
);

clearBtn.addEventListener(
    "click",
    function () {

        fileInput.value = "";

        fileName.innerText =
        "No file selected";

    }
);

summarizeBtn.addEventListener(
    "click",
    async function () {

        console.log("BUTTON CLICKED");

        if(fileInput.files.length === 0){

            alert("Please select a file");
            return;

        }

        const formData = new FormData();

        formData.append(
            "file",
            fileInput.files[0]
        );

        console.log("Sending request...");

        try {

            const response =
            await fetch(
                "https://ai-powered-video-summarization-system.onrender.com/upload",
                {
                    method: "POST",
                    body: formData
                }
            );

            console.log(
                "STATUS:",
                response.status
            );

            const data =
            await response.json();

            document.getElementById(
                "resultContainer"
            ).style.display = "block";

            document.getElementById(
                "title"
            ).innerText =
            data.title;

            document.getElementById(
                "overview"
            ).innerText =
            data.summary.overview;

            document.getElementById(
                "problem"
            ).innerText =
            data.summary.problem;

            document.getElementById(
                "solution"
            ).innerText =
            data.summary.solution;

            const keyPoints =
            document.getElementById(
                "keyPoints"
            );

            keyPoints.innerHTML = "";

            data.key_points.forEach(
                function(item){

                    const li =
                    document.createElement(
                        "li"
                    );

                    li.innerText =
                    item.point;

                    keyPoints.appendChild(
                        li
                    );

                }
            );

            const actionItems =
            document.getElementById(
                "actionItems"
            );

            actionItems.innerHTML = "";

            data.action_items.forEach(
                function(item){

                const li =
                document.createElement(
                    "li"
                );

                li.innerText =
                item.action;

                actionItems.appendChild(
                     li
                );

            }
        );

            console.log(
                "DATA RECEIVED:"
            );

            console.log(data);

            //alert(
            //    "Response received. Check Console."
            //);

        }
        catch(error){

            console.error(
                "FETCH ERROR:",
                error
            );

        }

    }
);
