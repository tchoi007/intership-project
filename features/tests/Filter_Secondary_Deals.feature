Feature: Filter Secondary deals

  Scenario: User can filter secondary deals by "want to sell" option
    Given Open the main page
    When Log in to the page
    And Click on the Secondary option
    And Verify the right page opens
    And Click on filters
    And Filter the products by "want to sell"
    And click on apply filter
    Then Verify all cards have for sale tag