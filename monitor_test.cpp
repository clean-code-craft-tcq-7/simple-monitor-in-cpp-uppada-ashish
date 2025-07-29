#include <gtest/gtest.h>
#include "./monitor.h"

TEST(VitalsTest, ReturnsFalseWhenAnyVitalIsOutOfRange) {
  // Pulse rate is too high
  EXPECT_FALSE(areVitalsOk(99, 102, 70));
}

TEST(VitalsTest, ReturnsTrueWhenAllVitalsAreNormal) {
  EXPECT_TRUE(areVitalsOk(98.1, 70, 98));
}