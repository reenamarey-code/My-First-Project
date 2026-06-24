document.getElementById("form").addEventListener("submit", async function(e) {
    e.preventDefault();

    const inputs = document.querySelectorAll("input");

    const data = {
        pregnancies: Number(inputs[0].value),
        glucose: Number(inputs[1].value),
        blood_pressure: Number(inputs[2].value),
        skin_thickness: Number(inputs[3].value),
        insulin: Number(inputs[4].value),
        bmi: Number(inputs[5].value),
        pedigree: Number(inputs[6].value),
        age: Number(inputs[7].value)
    };

    try {
        const res = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await res.json();

        document.getElementById("result").innerText =
            result.prediction === 1 ? "⚠️ Diabetic" : "✅ Not Diabetic";

        document.getElementById("confidence").innerText =
            "Confidence: " + result.confidence + "%";

    } catch (err) {
        document.getElementById("result").innerText = "❌ Server Error";
        console.error(err);
    }
});