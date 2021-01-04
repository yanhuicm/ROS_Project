// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from realsense_camera_msgs:msg/Extrinsics.idl
// generated code does not contain a copyright notice

#ifndef REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__FUNCTIONS_H_
#define REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_generator_c/visibility_control.h"
#include "realsense_camera_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "realsense_camera_msgs/msg/extrinsics__struct.h"

/// Initialize msg/Extrinsics message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * realsense_camera_msgs__msg__Extrinsics
 * )) before or use
 * realsense_camera_msgs__msg__Extrinsics__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
bool
realsense_camera_msgs__msg__Extrinsics__init(realsense_camera_msgs__msg__Extrinsics * msg);

/// Finalize msg/Extrinsics message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
void
realsense_camera_msgs__msg__Extrinsics__fini(realsense_camera_msgs__msg__Extrinsics * msg);

/// Create msg/Extrinsics message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * realsense_camera_msgs__msg__Extrinsics__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
realsense_camera_msgs__msg__Extrinsics *
realsense_camera_msgs__msg__Extrinsics__create();

/// Destroy msg/Extrinsics message.
/**
 * It calls
 * realsense_camera_msgs__msg__Extrinsics__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
void
realsense_camera_msgs__msg__Extrinsics__destroy(realsense_camera_msgs__msg__Extrinsics * msg);


/// Initialize array of msg/Extrinsics messages.
/**
 * It allocates the memory for the number of elements and calls
 * realsense_camera_msgs__msg__Extrinsics__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
bool
realsense_camera_msgs__msg__Extrinsics__Sequence__init(realsense_camera_msgs__msg__Extrinsics__Sequence * array, size_t size);

/// Finalize array of msg/Extrinsics messages.
/**
 * It calls
 * realsense_camera_msgs__msg__Extrinsics__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
void
realsense_camera_msgs__msg__Extrinsics__Sequence__fini(realsense_camera_msgs__msg__Extrinsics__Sequence * array);

/// Create array of msg/Extrinsics messages.
/**
 * It allocates the memory for the array and calls
 * realsense_camera_msgs__msg__Extrinsics__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
realsense_camera_msgs__msg__Extrinsics__Sequence *
realsense_camera_msgs__msg__Extrinsics__Sequence__create(size_t size);

/// Destroy array of msg/Extrinsics messages.
/**
 * It calls
 * realsense_camera_msgs__msg__Extrinsics__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_realsense_camera_msgs
void
realsense_camera_msgs__msg__Extrinsics__Sequence__destroy(realsense_camera_msgs__msg__Extrinsics__Sequence * array);

#ifdef __cplusplus
}
#endif

#endif  // REALSENSE_CAMERA_MSGS__MSG__EXTRINSICS__FUNCTIONS_H_
