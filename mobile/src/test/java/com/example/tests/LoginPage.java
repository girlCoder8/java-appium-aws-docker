package pages;

import io.appium.java_client.AppiumBy;
import io.appium.java_client.ios.IOSDriver;
import org.openqa.selenium.WebElement;

public class LoginPage {
    private IOSDriver driver;

    // Locators for iOS elements (update accessibility ids as per your app)
    private final String usernameFieldId = "username_input";
    private final String passwordFieldId = "password_input";
    private final String loginButtonId = "login_button";
    private final String errorMessageId = "error_message";

    public LoginPage(IOSDriver driver) {
        this.driver = driver;
    }

    public void enterUsername(String username) {
        WebElement usernameField = driver.findElement(AppiumBy.accessibilityId(usernameFieldId));
        usernameField.clear();
        usernameField.sendKeys(username);
    }

    public void enterPassword(String password) {
        WebElement passwordField = driver.findElement(AppiumBy.accessibilityId(passwordFieldId));
        passwordField.clear();
        passwordField.sendKeys(password);
    }

    public void tapLoginButton() {
        driver.findElement(AppiumBy.accessibilityId(loginButtonId)).click();
    }

    public String getErrorMessage() {
        return driver.findElement(AppiumBy.accessibilityId(errorMessageId)).getText();
    }
}