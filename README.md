# ROBE-313 Final Project: The Scout Package

This repository contains the foundational ROS 2 package for your Final Project rover. It includes the `base_link` and `right_wheel` to get you started.

## The Objective
Complete the kinematic tree for the Scout Rover so it can be deployed into Gazebo for the ArUco scavenger hunt.

## Assessment Requirements
1. **Complete the URDF:** Open `urdf/scout.urdf` and add the following missing elements:
   * A `left_wheel` (mirroring the right wheel).
   * A `caster_wheel` attached to the rear of the chassis for stability.
   * A `camera_link` attached to the front of the chassis.
2. **Build the Package:** Compile your workspace to ensure the `setup.py` correctly installs your updated URDF.
3. **Visualize:** Verify the complete model loads without errors in RViz using the `urdf_tutorial` launch file.

## Submission
Commit your changes and push them back to this repository. All group members must contribute to the repository to receive full credit.

```bash
git add .
git commit -m "Completed URDF chassis with all wheels and camera"
git push origin main
