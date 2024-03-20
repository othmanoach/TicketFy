document.addEventListener('DOMContentLoaded', (event) => {
    const canvas = document.getElementById('myCanvas');
    if (canvas.getContext) {
        const ctx = canvas.getContext('2d');

        let time = 0;
        const width = canvas.width;
        const height = canvas.height;
        const scale = 100; // Scale for the curve

        function draw() {
            // Clear the canvasa
            ctx.clearRect(0, 0, width, height);

            // Parameters for the Lissajous curve
            const xFrequency = 4;
            const yFrequency = 3;
            const xPhase = 0;
            const yPhase = Math.PI / 2; // 90 degrees phase shift

            // Calculate the new x and y position
            const x = width / 2 + scale * Math.sin(xFrequency * time + xPhase);
            const y = height / 2 + scale * Math.sin(yFrequency * time + yPhase);

            // Draw the Lissajous curve
            ctx.beginPath();
            ctx.arc(x, y, 5, 0, Math.PI * 2); // Draw a circle at the x, y position
            ctx.fillStyle = 'red';
            ctx.fill();

            // Update the time for the next frame
            time += 0.05;

            // Request the next frame of the animation
            requestAnimationFrame(draw);
        }

        // Start the animation
        draw();
    }
});
