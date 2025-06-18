document.addEventListener('DOMContentLoaded', () => {
    // --- GSAP Animations ---

    // Check if GSAP is available
    if (typeof gsap === 'undefined') {
        console.warn('GSAP library is not loaded. Animations will not run.');
        return;
    }

    // 1. Menu Item Entrance Animation (on menu.html)
    // Check if we are on the menu page by looking for #foodItems container
    const foodItemsContainer = document.getElementById('foodItems');
    if (foodItemsContainer) {
        const menuItems = foodItemsContainer.querySelectorAll('.menu-item');
        if (menuItems.length > 0) {
            gsap.from(menuItems, {
                opacity: 0,
                y: 30, // Start 30px down
                duration: 0.6,
                stagger: 0.15, // Stagger the start of each animation by 0.15s
                ease: 'power2.out'
            });
        }
    }

    // 2. Button Hover Animations (for .btn-ui-primary and .btn-ui-secondary)
    const primaryButtons = document.querySelectorAll('.btn-ui-primary');
    const secondaryButtons = document.querySelectorAll('.btn-ui-secondary');

    const allStyledButtons = [...primaryButtons, ...secondaryButtons];

    allStyledButtons.forEach(button => {
        // Store original scale
        const originalScale = 1;
        gsap.set(button, { transformOrigin: 'center center' }); // Ensure scaling is from center

        button.addEventListener('mouseenter', () => {
            gsap.to(button, {
                scale: 1.05, // Scale up slightly
                duration: 0.2,
                ease: 'power1.out'
            });
        });

        button.addEventListener('mouseleave', () => {
            gsap.to(button, {
                scale: originalScale, // Return to original scale
                duration: 0.2,
                ease: 'power1.inOut'
            });
        });

        // Optional: Add a subtle press effect
        button.addEventListener('mousedown', () => {
            gsap.to(button, { scale: originalScale * 0.95, duration: 0.1, ease: 'power1.out' });
        });
        button.addEventListener('mouseup', () => {
            // Could also be mouseleave for this one if mouse is dragged off while pressed
            gsap.to(button, { scale: originalScale * 1.05, duration: 0.1, ease: 'power1.inOut' });
        });
         button.addEventListener('mouseout', () => { // Ensure it returns to normal if mouse leaves while pressed
            if(gsap.getProperty(button, "scale") < originalScale) {
                 gsap.to(button, { scale: originalScale, duration: 0.2, ease: 'power1.inOut' });
            }
        });
    });

    // Example: General page fade-in for all pages (subtle)
    // Could be too much if not desired, but here's an example
    // const mainContent = document.querySelector('main'); // Or body
    // if (mainContent) {
    //    gsap.from(mainContent, { opacity: 0, duration: 0.5, ease: 'power1.in' });
    // }


    console.log('GSAP animations initialized.');
});
