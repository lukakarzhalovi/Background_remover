import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

def object_detenction_on_image():
    mysegmentImage = instanceSegmentation()
    mysegmentImage.load_model("pointrend_resnet50.pkl")
    target_class = mysegmentImage.select_target_classes()

    result = mysegmentImage.segmentImage( #აქვს ორი აუცილებელი პარამეტრი
        image_path = "static/uploaded_image.png",
        show_bboxes= True,
        # extract_segmented_objects= True,
        # save_extracted_objects= True,
        # segment_target_classes = target_class,
        output_image_name = "static/result.png"
    )

def object_detenction_on_video():
    mysegmentVideo = instanceSegmentation()
    mysegmentVideo.load_model("pointrend_resnet50.pkl")

    mysegmentVideo.process_video(
        video_path= 'car.mp4',
        show_bboxes= True,
        frames_per_second = 15,
        output_video_name = 'car_sec.mp4'
    )

# def main():
#     object_detenction_on_image()
#     # object_detenction_on_video()
