jQuery(document).ready(function () {
  jQuery("#gallery").nanogallery2({
    items:
      data
    ,
    thumbnailWidth: "auto",
    thumbnailHeight: 400,
    thumbnailLabel: { display: false },
    itemsBaseURL:
      "https://raw.githubusercontent.com/mwiens91/misha-pics/master/pics",
    viewerTools: {
      topLeft: "label",
      topRight: "zoomButton, fullscreenButton, downloadButton, closeButton",
    },
  });
});
