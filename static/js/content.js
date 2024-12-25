function shareTo(url) {
    const pageUrl = window.location.href; // لینک فعلی صفحه
    window.open(url.replace('PAGE_URL', encodeURIComponent(pageUrl)), '_blank');
}