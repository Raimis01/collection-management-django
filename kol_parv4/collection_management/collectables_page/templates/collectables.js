document.addEventListener('DOMContentLoaded', function() {
    const observer = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) {
            fetchNextPage();
        }
    }, { threshold: 0.5 });

    const sentinel = document.getElementById('sentinel');
    observer.observe(sentinel);

    let nextPage = 2;
    let inFlight = false;

    function fetchNextPage() {
        if (inFlight) return;
        inFlight = true;
        
        const url = `/path/to/your/view/?page=${nextPage}`;
        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.html) {
                document.querySelector('#itemTable tbody').insertAdjacentHTML('beforeend', data.html);
                if (data.has_more) {
                    nextPage++;
                } else {
                    observer.disconnect();
                    sentinel.remove();
                }
            }
            inFlight = false;
        })
        .catch(error => {
            console.error('Error loading more items:', error);
            inFlight = false;
        });
    }
});