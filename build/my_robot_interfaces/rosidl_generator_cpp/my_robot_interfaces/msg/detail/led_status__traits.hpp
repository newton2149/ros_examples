// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from my_robot_interfaces:msg/LedStatus.idl
// generated code does not contain a copyright notice

#ifndef MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__TRAITS_HPP_
#define MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__TRAITS_HPP_

#include "my_robot_interfaces/msg/detail/led_status__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<my_robot_interfaces::msg::LedStatus>()
{
  return "my_robot_interfaces::msg::LedStatus";
}

template<>
inline const char * name<my_robot_interfaces::msg::LedStatus>()
{
  return "my_robot_interfaces/msg/LedStatus";
}

template<>
struct has_fixed_size<my_robot_interfaces::msg::LedStatus>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<my_robot_interfaces::msg::LedStatus>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<my_robot_interfaces::msg::LedStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MY_ROBOT_INTERFACES__MSG__DETAIL__LED_STATUS__TRAITS_HPP_
