import os
import shutil


def train_test_split_folder(path: str, output_path:str, test_split_size: float) -> None:
    """
        Takes in a path of data and divides it into training 
        and test subfolders. The data structure should be:\n
        data -> class 1 -> images_from_class_1\n
             -> class 2 -> images_from_class_2\n
             ...\n
             -> class n -> images_from_class_n\n
        Args:
            path: path to the datafolder
            split_size: float that contains the % of test size
        Returns:
            None
    """

    # Get the class names listing the main folder
    classes = os.listdir(path)

    # Create the train and test path based on the output_path
    train_path = os.path.join(output_path, "train")
    test_path = os.path.join(output_path, "test")

    # Create the test and train directories
    os.mkdir(test_path)
    os.mkdir(train_path)

    # Walk through every class
    for class_name in classes:

        print(f"Current class: {class_name}")
        # Create the train folder for the class
        class_path_train = os.path.join(train_path, class_name)
        os.mkdir(class_path_train)

        # Do the same for test
        class_path_test = os.path.join(test_path, class_name)
        os.mkdir(class_path_test)

        # Walk through every file in the class path
        images = os.listdir(os.path.join(path, class_name))

        # Define the split size
        split_size = round(len(images) * test_split_size)

        # Divide the images based on the split_size
        train_images = images[split_size:]
        test_images = images[:split_size]

        # Walk through train images
        for image in train_images:
            # Move the image to the train path
            src = os.path.join(path, class_name, image)
            dst = os.path.join(class_path_train, image)
            shutil.move(src, dst)

        # Now for test
        for image in test_images:
            # Move the image to the train path
            src = os.path.join(path, class_name, image)
            dst = os.path.join(class_path_test, image)
            shutil.move(src, dst)
