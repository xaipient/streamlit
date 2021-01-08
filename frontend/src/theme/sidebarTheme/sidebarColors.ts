import { transparentize } from "color2k"
import { colors } from "../primitives/colors"

const genericColors = {
  ...colors,
  bodyText: "#ffffff",
  danger: "#ff9191",
  info: "#86cfda",
  success: "#7fd399",
  warning: "#f9e39c",
  primary: "#bdcdff",
  tagBg: "#7792e3",
  disabled: colors.gray30,
  secondary: colors.gray60,
  lightestGray: colors.gray20,
  lightGray: colors.gray30,
  gray: colors.gray60,
  darkGray: colors.gray70,
  red: colors.red80,
  blue: colors.blue80,
  green: colors.green80,
  yellow: colors.yellow80,
}

export default {
  ...genericColors,
  backgroundImage:
    "url(" +
    "https://raw.githubusercontent.com/youozhan/design-ai/master/Frame05.png" +
    ")",
  // Alerts
  alertErrorBorderColor: transparentize(genericColors.red, 0.8),
  alertErrorBackgroundColor: transparentize(genericColors.red, 0.8),
  alertErrorTextColor: genericColors.danger,
  alertInfoBorderColor: transparentize(genericColors.blue, 0.9),
  alertInfoBackgroundColor: transparentize(genericColors.blue, 0.9),
  alertInfoTextColor: genericColors.info,
  alertSuccessBorderColor: transparentize(genericColors.green, 0.8),
  alertSuccessBackgroundColor: transparentize(genericColors.green, 0.8),
  alertSuccessTextColor: genericColors.success,
  alertWarningBorderColor: transparentize(genericColors.yellow, 0.2),
  alertWarningBackgroundColor: transparentize(genericColors.yellow, 0.8),
  alertWarningTextColor: genericColors.warning,

  docStringHeaderBorder: "#e6e9ef",
  docStringModuleText: "#444444",
  docStringContainerBackground: "#f0f3f9",

  tableGray: colors.gray40,
}
