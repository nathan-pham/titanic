{
    /* <form action="/api/predict" method="POST"> */
}

const form = document.querySelector("form");
const inputs = [...form.querySelectorAll("input")];
const prediction = document.querySelector("#prediction");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const payload = inputs.reduce(
        (acc, input) => ({
            ...acc,
            [input.name]: input.value,
        }),
        {}
    );

    await fetch(form.getAttribute("action"), {
        method: form.getAttribute("method"),
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    })
        .then((res) => res.json())
        .then((res) => {
            prediction.textContent = res.prediction === 0 ? "die" : "survive";
        });
});
