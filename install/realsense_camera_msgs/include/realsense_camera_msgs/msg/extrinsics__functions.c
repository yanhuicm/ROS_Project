// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from realsense_camera_msgs:msg/Extrinsics.idl
// generated code does not contain a copyright notice
#include "realsense_camera_msgs/msg/extrinsics__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header__functions.h"

bool
realsense_camera_msgs__msg__Extrinsics__init(realsense_camera_msgs__msg__Extrinsics * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    realsense_camera_msgs__msg__Extrinsics__fini(msg);
    return false;
  }
  // rotation
  // translation
  return true;
}

void
realsense_camera_msgs__msg__Extrinsics__fini(realsense_camera_msgs__msg__Extrinsics * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // rotation
  // translation
}

realsense_camera_msgs__msg__Extrinsics *
realsense_camera_msgs__msg__Extrinsics__create()
{
  realsense_camera_msgs__msg__Extrinsics * msg = (realsense_camera_msgs__msg__Extrinsics *)malloc(sizeof(realsense_camera_msgs__msg__Extrinsics));
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(realsense_camera_msgs__msg__Extrinsics));
  bool success = realsense_camera_msgs__msg__Extrinsics__init(msg);
  if (!success) {
    free(msg);
    return NULL;
  }
  return msg;
}

void
realsense_camera_msgs__msg__Extrinsics__destroy(realsense_camera_msgs__msg__Extrinsics * msg)
{
  if (msg) {
    realsense_camera_msgs__msg__Extrinsics__fini(msg);
  }
  free(msg);
}


bool
realsense_camera_msgs__msg__Extrinsics__Sequence__init(realsense_camera_msgs__msg__Extrinsics__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  realsense_camera_msgs__msg__Extrinsics * data = NULL;
  if (size) {
    data = (realsense_camera_msgs__msg__Extrinsics *)calloc(size, sizeof(realsense_camera_msgs__msg__Extrinsics));
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = realsense_camera_msgs__msg__Extrinsics__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        realsense_camera_msgs__msg__Extrinsics__fini(&data[i - 1]);
      }
      free(data);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
realsense_camera_msgs__msg__Extrinsics__Sequence__fini(realsense_camera_msgs__msg__Extrinsics__Sequence * array)
{
  if (!array) {
    return;
  }
  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      realsense_camera_msgs__msg__Extrinsics__fini(&array->data[i]);
    }
    free(array->data);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

realsense_camera_msgs__msg__Extrinsics__Sequence *
realsense_camera_msgs__msg__Extrinsics__Sequence__create(size_t size)
{
  realsense_camera_msgs__msg__Extrinsics__Sequence * array = (realsense_camera_msgs__msg__Extrinsics__Sequence *)malloc(sizeof(realsense_camera_msgs__msg__Extrinsics__Sequence));
  if (!array) {
    return NULL;
  }
  bool success = realsense_camera_msgs__msg__Extrinsics__Sequence__init(array, size);
  if (!success) {
    free(array);
    return NULL;
  }
  return array;
}

void
realsense_camera_msgs__msg__Extrinsics__Sequence__destroy(realsense_camera_msgs__msg__Extrinsics__Sequence * array)
{
  if (array) {
    realsense_camera_msgs__msg__Extrinsics__Sequence__fini(array);
  }
  free(array);
}
