from deepclean.couplings import Coupling, SubtractionProblem


class Sub120Hz(SubtractionProblem):
    description = "Subtraction of 120Hz main noise and side bands"

    H1 = Coupling(
        110,
        130,
        [
            "PEM-CS_ACC_PSL_TABLE1_Z_DQ",
            "HPI-HAM4_BLND_L4C_Y_IN1_DQ",
            "IMC-WFS_A_Q_PIT_OUT_DQ",
            "IMC-WFS_B_Q_PIT_OUT_DQ",
            "IMC-DOF_1_Y_IN1_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_X_DQ",
            "IMC-DOF_4_Y_IN1_DQ",
            "HPI-HAM6_BLND_L4C_RX_IN1_DQ",
            "IMC-WFS_A_DC_YAW_OUT_DQ",
            "IMC-WFS_B_I_PIT_OUT_DQ",
            "IMC-WFS_B_Q_YAW_OUT_DQ",
            "IMC-WFS_A_Q_YAW_OUT_DQ",
            "PSL-PMC_HV_MON_OUT_DQ",
            "LSC-REFL_SERVO_ERR_OUT_DQ",
            "IMC-WFS_B_I_YAW_OUT_DQ",
            "PEM-CS_ACC_HAM2_PRM_Z_DQ",
            "PEM-CS_ACC_PSL_TABLE1_X_DQ",
            "LSC-MCL_IN1_DQ",
            "IMC-WFS_A_DC_PIT_OUT_DQ",
            "IMC-F_OUT_DQ",
            "LSC-REFL_SERVO_CTRL_OUT_DQ",
            "PSL-PMC_MIXER_OUT_DQ",
            "IMC-WFS_B_DC_YAW_OUT_DQ",
            "PEM-CS_ACC_PSL_PERISCOPE_Y_DQ",
            "IMC-DOF_2_Y_IN1_DQ",
            "LSC-MCL_OUT_DQ",
            "HPI-HAM1_BLND_L4C_RX_IN1_DQ",
            "HPI-HAM6_BLND_L4C_VP_IN1_DQ",
            "IMC-DOF_2_P_IN1_DQ",
            "IMC-L_OUT_DQ",
            "PEM-CS_ACC_LVEAFLOOR_BS_Z_DQ",
            "PEM-CS_ACC_HAM2_PRM_Y_DQ",
            "PEM-CS_ACC_LVEAFLOOR_HAM1_X_DQ",
            "HPI-HAM2_BLND_L4C_RY_IN1_DQ",
            "HPI-HAM1_BLND_L4C_VP_IN1_DQ",
        ],
    )
